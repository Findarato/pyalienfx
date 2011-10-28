import platform
import sys,os

class AlienFXProperties:
	def __init__(self):
		self.isDebug = False
		
		self.AUTHOR = "Blondel Leo"
		
		#Application info
		self.ALIEN_FX_VERSION = "pre alpha"
		self.ALIEN_FX_APPLICATION_RAW_NAME = "pyAlienFX"
		self.ALIEN_FX_APPLICATION_NAME = self.ALIEN_FX_APPLICATION_RAW_NAME +" "+ self.ALIEN_FX_VERSION
		
		#java properties
		self.PROPERTY_OS_NAME = platform.platform()
		self.USER_HOME = os.path.expanduser('~')
		self.JAVA_ARCHITECTURE = platform.machine()
		
		#used properties
		self.arch = platform.machine()
		self.userHomePath = os.path.expanduser('~')
		self.osName = sys.platform
		
		#OS checks
		self.WINDOWS_OS = "Windows"
		self.isWindows = self.isWindows()

		#native libraries
		self.ALIENFX_NATIVE_LIBRARY_NAME = "Alien"
		self.ALIENFX_NATIVE_LIBRARY = self.ALIENFX_NATIVE_LIBRARY_NAME+self.arch
		
		#powermodes and region ids
		self.ALIEN_FX_DEFAULT_POWER_MODE = ""
		self.POWER_BUTTON_ID = "PB"
		self.POWER_BUTTON_EYES_ID = "PBE"
		self.MEDIA_BAR_ID = "MB"
		self.TOUCH_PAD_ID = "TP"
		self.ALIEN_LOGO_ID = "AL"
		self.ALIEN_HEAD_ID = "AH"
		self.LEFT_SPEAKER_ID = "LS"
		self.RIGHT_SPEAKER_ID = "RS"
		self.LEFT_CENTER_KEYBOARD_ID = "LCK"
		self.LEFT_KEYBOARD_ID = "LK"
		self.RIGHT_CENTER_KEYBOARD_ID = "RCK"
		self.RIGHT_KEYBOARD_ID = "RK"
		self.LIGHT_PIPE_ID = "LP"
		self.KEYBOARD_ID = "KB"
		
		self.ON_BATTERY_ID = "BAT"
		self.CHARGING_ID = "CH"
		self.AC_POWER_ID = "AC"
		self.STANDBY_ID = "SB"
		
	def isWindows(self):
		if self.WINDOWS_OS in platform.platform():
			return True
		return False