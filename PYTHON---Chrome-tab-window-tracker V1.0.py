import pyautogui
import time

def get_open_chrome_tabs():
    # Bring Chrome to the foreground
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)  # Wait for the switch to complete

    # Open the Chrome menu
    pyautogui.hotkey('ctrl', 'l')  # Select the address bar
    pyautogui.typewrite('chrome://history')  # Type the address
    pyautogui.press('enter')  # Press Enter to open history page
    time.sleep(2)  # Wait for the history page to load

    # Get the position of the first tab
    chrome_icon_pos = pyautogui.locateOnScreen('chrome_icon.png', confidence=0.9)
    if chrome_icon_pos:
        tab_pos = (chrome_icon_pos[0] - 200, chrome_icon_pos[1] + 100)
    else:
        print("Chrome icon not found. Make sure Chrome is open and try again.")
        return []

    # Click on the first tab
    pyautogui.click(tab_pos)

    # Scroll down to load more history entries
    for _ in range(5):
        pyautogui.scroll(-100)

    # Find and click on the "Tabs from other devices" link if it exists
    tabs_from_other_devices = pyautogui.locateOnScreen('tabs_from_other_devices.png', confidence=0.9)
    if tabs_from_other_devices:
        pyautogui.click(tabs_from_other_devices)

    # Find and click on the "Tabs" tab
    tabs_tab_pos = pyautogui.locateCenterOnScreen('tabs_tab.png', confidence=0.9)
    if tabs_tab_pos:
        pyautogui.click(tabs_tab_pos)
    else:
        print("Could not find the 'Tabs' tab. Make sure Chrome history is open and try again.")
        return []

    # Scroll down to load all open tabs
    for _ in range(10):
        pyautogui.scroll(100)

    # Find and click on the "Tabs" list
    tabs_list_pos = pyautogui.locateCenterOnScreen('tabs_list.png', confidence=0.9)
    if tabs_list_pos:
        pyautogui.click(tabs_list_pos)
    else:
        print("Could not find the list of tabs. Make sure Chrome history is open and try again.")
        return []

    # Get the list of open tabs
    open_tabs = []
    for i in range(1, 100):
        tab_pos = pyautogui.locateCenterOnScreen('tab{}.png'.format(i), confidence=0.9)
        if tab_pos:
            open_tabs.append("Tab {}: ({}, {})".format(i, tab_pos[0], tab_pos[1]))
        else:
            break

    # Close the Chrome history tab
    pyautogui.hotkey('ctrl', 'w')  # Close the tab

    return open_tabs

# Example usage
if __name__ == "__main__":
    open_tabs = get_open_chrome_tabs()
    print("Open Chrome Tabs:")
    for tab in open_tabs:
        print(tab)
