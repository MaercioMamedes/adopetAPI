def validate_name(fullname):
    """Verifica se algum caracter do nome digitado é numérico"""

    for element in fullname.split():
        if any(character.isdigit() for character in element):
            return False
        
    return True

def validate_password(password):
    """Verifica se a senha cadastrada tem algum caracter espaço"""

    if ' ' in password:
        return False
    
    else:
        return True

def validate_image(image):
    """Verifica se a imagem é jpg ou png. Se for diferente retorna False"""
    
    return image.content_type != 'image/jpeg' and image.content_type != 'image/png'