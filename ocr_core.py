try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))

    if(text.find('International') != -1):
    	return "International Payment"
    elif(text.find('Domestic') != -1):
    	return "Domestic Payment"
    else:
	    return "Some other payment"

	