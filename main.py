import numpy as np
import cv2
from scipy.ndimage import convolve, minimum_filter, maximum_filter, median_filter
from matplotlib import pyplot as plt


# Filtros básicos
def average_filter(image, kernel_size):
    """Aplica un filtro de promedio."""
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    return convolve(image, kernel)


def median_filter_custom(image, kernel_size):
    """Aplica un filtro de mediana."""
    return median_filter(image, size=kernel_size)


def maximum_filter_custom(image, kernel_size):
    """Aplica un filtro de máximo."""
    return maximum_filter(image, size=kernel_size)


def minimum_filter_custom(image, kernel_size):
    """Aplica un filtro de mínimo."""
    return minimum_filter(image, size=kernel_size)


# Filtro de gradiente
def gradient_filter(image, kernel_size=3):
    """Aplica un filtro de gradiente morfológico."""
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)


# Filtro Laplaciano
def laplacian_filter(image, variant="direct"):
    """Aplica un filtro Laplaciano a una imagen."""
    image = image.astype(float)
    output = np.zeros_like(image)
    rows, cols = image.shape

    if variant == "direct":
        for f in range(1, rows - 1):
            for c in range(1, cols - 1):
                output[f, c] = (
                    image[f - 1, c] + image[f, c - 1] - 4 * image[f, c]
                    + image[f, c + 1] + image[f + 1, c]
                )
    elif variant == "diagonal":
        for f in range(1, rows - 1):
            for c in range(1, cols - 1):
                output[f, c] = (
                    image[f - 1, c - 1] + image[f - 1, c] + image[f - 1, c + 1]
                    + image[f, c - 1] - 8 * image[f, c]
                    + image[f, c + 1] + image[f + 1, c - 1]
                    + image[f + 1, c] + image[f + 1, c + 1]
                )
    else:
        raise ValueError("Invalid variant. Choose 'direct' or 'diagonal'.")

    return np.clip(output, 0, 255).astype(np.uint8)


# Función principal
if __name__ == "__main__":
    while True:
        # Selección de imagen
        print("\nSelecciona la imagen que deseas usar:")
        print("1. Alto contraste")
        print("2. Bajo contraste")
        print("3. Alta iluminación")
        print("4. Baja iluminación")
        print("0. Salir")

        try:
            image_option = int(input("Ingresa el número de la imagen: "))
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
            continue

        if image_option == 0:
            print("Saliendo del programa...")
            break

        image_files = {
            1: "altoContraste2.jpg",
            2: "conba.jpg",
            3: "altaIluminacion2.jpg",
            4: "bajaIluminacion.jpg"
        }

        if image_option not in image_files:
            print("Opción de imagen no válida. Inténtalo de nuevo.")
            continue

        image_path = image_files[image_option]
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print(f"No se pudo cargar la imagen '{image_path}'. Verifica el archivo.")
            continue

        # Menú de filtros
        while True:
            print("\nSelecciona el filtro que deseas aplicar:")
            print("1. Promedio")
            print("2. Mediana")
            print("3. Máximo")
            print("4. Mínimo")
            print("5. Laplaciano")
            print("6. Gradiente")
            print("0. Volver al menú de imágenes")

            try:
                option = int(input("Ingresa una opción: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if option == 0:
                break

            if option in [1, 2, 3, 4]:
                try:
                    kernel_size = int(input("Ingresa el tamaño de la máscara (un solo dígito): "))
                except ValueError:
                    print("Por favor, ingresa un número válido para la máscara.")
                    continue
                if kernel_size < 3:
                    print("El tamaño de la máscara debe ser al menos 3.")
                    continue

            if option == 1:  # Promedio
                result = average_filter(image, kernel_size)
                title = f"Filtro de Promedio {kernel_size}x{kernel_size}"
            elif option == 2:  # Mediana
                result = median_filter_custom(image, kernel_size)
                title = f"Filtro de Mediana {kernel_size}x{kernel_size}"
            elif option == 3:  # Máximo
                result = maximum_filter_custom(image, kernel_size)
                title = f"Filtro de Máximo {kernel_size}x{kernel_size}"
            elif option == 4:  # Mínimo
                result = minimum_filter_custom(image, kernel_size)
                title = f"Filtro de Mínimo {kernel_size}x{kernel_size}"
            elif option == 5:  # Laplaciano
                result = laplacian_filter(image, variant="direct")
                title = "Filtro Laplaciano (Directo)"
            elif option == 6:  # Gradiente
                result = gradient_filter(image)
                title = "Filtro de Gradiente"
            else:
                print("Opción no válida. Inténtalo de nuevo.")
                continue

            # Mostrar resultados
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.imshow(image, cmap='gray')
            plt.title("Imagen Original")
            plt.axis('off')

            plt.subplot(1, 2, 2)
            plt.imshow(result, cmap='gray')
            plt.title(title)
            plt.axis('off')

            plt.tight_layout()
            plt.show()
