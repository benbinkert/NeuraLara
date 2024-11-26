#  Verbinden des Roboters über Ethernet mit Rviz:

##  Schritte:
 **Vorbereitung:** ROS Interface auf dem Tablet aktivieren
1. export ROS_MASTER_URI=http://192.168.2.13:11311/ <br/>
   export ROS_IP=192.168.2.12<br/>
   roslaunch neura_moveitconfig_ben  lara5_moveit_planning_execution.launch<br/>

3. in Rviz auf scene object dann auf die auswahl neben dem plus und mesh from file, dann in den ROS ordner und die STL datei auswählen.<br/>
   **Wichtig** ist sofort auf publish zu drücken und nach jedem Verändern der Kordinaten des Objects wieder auf publish zu drücken sonst abstutz. <br/>
    **Wichtig** ist das der Stromanschluss des Roboters wie in echt nach hinten in den Wagen zeigt, sonst falsche coliision zones

4.  Dann auf das planning tab wechseln,  den Roboter in die Position bewegen auf plan drücken und nach der berechnung auf execute<br/>
     **Probleme**: kann teilweise auftreten das eine Fehlermeldung kommt weil die Abweichung der Roboter position zu groß ist.
		einfach auf eine andere Position bewegen und erneut planen und executen

**Hinweis:** bitte keine bash befehle autospeichern hat schon zu problemen mit Ros geführt

# Nächstes Ziele: 
 mit rosrun eine python datei auszuführen und diese bewegt den roboter. Ordner dafür wäre im im neura_moveitconfig_ben der scripts ordner
