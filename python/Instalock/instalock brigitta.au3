HotKeySet ("{F1}", "myExit")
while (1)
pick()
WEnd
Func pick()
	$pixels = PixelSearch(1509, 867,1519, 939,0xFFE2A8,10)



	if NOT(@error) Then
		MouseClick("left",1510, 900,1,1) ;Brigitta
		MouseClick("left",960, 1009,1,1) ;lock hero
		sleep (1000)
		$pixels2 = PixelSearch(195, 982,201, 999,0x6B3C31,5)
		if NOT(@error) Then
			myExit()
		EndIf

	EndIf
EndFunc
Func myExit()


	Exit
EndFunc