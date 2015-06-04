from colorama import Fore, Back, Style, init
import datetime

init(autoreset=True)

def logInformation(textToPrint):
	prefix = 'LOG ' + datetime.time.isoformat(datetime.datetime.now().time()) + ':    '
	print(Fore.BLACK + Back.GREEN + Style.BRIGHT + prefix + textToPrint)


logInformation('Hello, World!')


def logWarning(textToPrint):
	prefix = 'WAR ' + datetime.time.isoformat(datetime.datetime.now().time()) + ':    '
	print(Fore.BLACK + Back.YELLOW + Style.BRIGHT + prefix + textToPrint)


logWarning('Hello, World!')