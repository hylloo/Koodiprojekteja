HotKeySet ("{F6}", "_Start")
HotKeySet ("{F2}", "myExit")
$x = WinActivate("Counter-Strike: Global Offensive")

while(1)
	sleep(1000)
WEnd

Func _Start()

	$iCheckSum = PixelChecksum(952, 532,968, 548)

	While Not ($iCheckSum = PixelChecksum(952, 532,968, 548))
	MouseClick("left")
	sleep(100)
	WEnd

EndFunc

Func myExit()
	Exit
EndFunc