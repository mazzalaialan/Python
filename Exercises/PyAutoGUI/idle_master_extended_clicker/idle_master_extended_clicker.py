import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

def main():
    """Runs the entire program. The Sushi Go Round game must be visible on the screen and the PLAY button visible."""
    logging.info('Program Started. Press Ctrl-C to abort at any time.')
    logging.info('To interrupt mouse movement, move mouse to upper left corner.')
    startClicking()


def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    os.chdir('c:\\users\\alan\\documents\\GitHub\\Python\\Exercises\\PyAutoGUI\\idle_master_extended_clicker')
    return os.path.join(os.getcwd(),'images', filename)

def startClicking():
    """Performs the clicks to navigate form the start screen (where the PLAY button is visible) to the beginning of the first level."""
    # Click on everything needed to get past the menus at the start of the game.

    # click on Play
    while True:
        logging.info('Looking for Next button...')
        posnext = pyautogui.locateCenterOnScreen(imPath('idle_master_autoclicker_next.png'))
        posicon = pyautogui.locateCenterOnScreen(imPath('icon.png'))
        if posnext is not None:
            pyautogui.click(posnext, duration=0.25)
            logging.info('Clicked on Next button.')
            pyautogui.move(posicon, duration=0.25)
        else:
            logging.info("Next button don't found.")
        time.sleep(10)


if __name__ == '__main__':
    main()