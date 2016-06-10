#!/usr/bin/python

import sys, getopt, time, glob, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def CreatePicoFile():
	picoFile = open(outputFile, "r+")
	content = picoFile.read().split('\n')

	line = GetLine(content, "__lua__") + 1
	endLine = GetLine(content, "__gfx__") - 1

	while content[line] != "__gfx__":
		content.remove(content[line])

	for file in glob.glob(inputFolder + "/*.lua"):
		c = open(file, "r").read()
		content.insert(line, "\n\n-- end " + file + "\n\n")
		content.insert(line, c)
		content.insert(line, "-- " + file + "\n\n")

	picoFile.seek(0)
	picoFile.truncate()

	for lines in content:
		picoFile.write(lines + "\n")

	picoFile.close()

def GetLine(file, phrase):
	for num, line in enumerate(file):
		if phrase in line:
			return num
	return -1
	
class ChangeHandler(PatternMatchingEventHandler):
	patterns = ["*.lua"]

	def on_modified(self, event):
		print event.src_path, event.event_type
		CreatePicoFile()



inputFolder=""
outputFile = ""

try:
	opts, args = getopt.getopt(sys.argv[1:], "hi:o", ["folder=", "output="])
except getopt.GetoptError:
	print 'python picocompiler.py --folder <inputFolder> --output <outputFile>'
	sys.exit(2)

for opt, arg, in opts:
	if opt in "-h":
		print 'python picocompiler.py -i <inputFolder> -o <outputFile>'
		sys.exit()
	elif opt in ("--folder"):
		inputFolder = arg
	elif opt in ("--output"):
		outputFile = arg

event_handler = ChangeHandler()
observer = Observer()
observer.schedule(event_handler, path=inputFolder, recursive=False)
observer.start()

print "Starting Pico Compiler!"

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
	print "Compiler stopped. Have a nice day."
observer.join()
