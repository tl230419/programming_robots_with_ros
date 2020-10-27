#!/usr/bin/env python

import pyttsx

engine = pyttsx.init()
engine.say('Sally sells seashells by the seasphore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()