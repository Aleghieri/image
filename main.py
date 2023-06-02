import cv2

def color_to_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def gray_to_binary(image, threshold):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image

# Carregar a imagem
image = cv2.imread("teferi.jpg")

# Verificar se a imagem foi carregada corretamente
if image is None:
    print("Falha ao carregar a imagem.")
    exit()

# Converter para níveis de cinza
gray_image = color_to_gray(image)

# Converter para binarizada
threshold_value = 127  # Define um valor de limiar (0-255)
binary_image = gray_to_binary(gray_image, threshold_value)

# Exibir as imagens
cv2.imshow("Imagem original", image)
cv2.imshow("Imagem em níveis de cinza", gray_image)
cv2.imshow("Imagem binarizada", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
