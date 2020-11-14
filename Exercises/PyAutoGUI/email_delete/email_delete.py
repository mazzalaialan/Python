import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

def main():
    """Runs the entire program. The Sushi Go Round game must be visible on the screen and the PLAY button visible."""
    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    """logging.info('To interrupt mouse movement, move mouse to upper left corner.')"""
    startClicking()


def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    os.chdir('c:\\users\\alan\\documents\\GitHub\\Python\\Exercises\\PyAutoGUI\\email_delete')
    return os.path.join(os.getcwd(),'images', filename)

def startClicking():
    """Performs the clicks to navigate form the start screen (where the PLAY button is visible) to the beginning of the first level."""
    # Click on everything needed to get past the menus at the start of the game.

    # click on Play
    poscheckbox = pyautogui.locateCenterOnScreen(imPath('checkbox.png'))
    posdelete = pyautogui.locateCenterOnScreen(imPath('delete.png'))
    while True:
        posaccept = None
        logging.info('Buscando si hay pendientes...')
        pospendings = pyautogui.locateCenterOnScreen(imPath('pendings.png'))
        if poscheckbox is not None and pospendings is not None and posdelete is not None:
            """posaccept = pyautogui.locateCenterOnScreen(imPath('accept.png'))"""
            pyautogui.click(poscheckbox, duration=0.01)
            logging.info('Clickeado en checkbox.')
            if posaccept is None:
                pyautogui.click(posdelete, duration=0.01)
                logging.info('Clickeado en eliminar.')
            else:
                pyautogui.click(posaccept, duration=0.01)
                logging.info('Clickeado en aceptar.')
        elif poscheckbox is None:
            logging.info("No se encontro el checkbox.")
        elif pospendings is None:
            logging.info("Bandeja de entrada vacia.")
        elif posdelete is None:
            logging.info("No se encontro el delete.")
        time.sleep(0.05)


if __name__ == '__main__':
    main()