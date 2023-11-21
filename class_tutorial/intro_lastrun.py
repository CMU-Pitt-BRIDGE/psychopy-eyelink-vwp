#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Tue Nov 21 12:00:57 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'intro'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/bridge-center/bridge/psychopy-eyelink-vwp/psychopy/intro_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "IntroText" ---
    intro_text = visual.TextStim(win=win, name='intro_text',
        text='Welcome to BRIDGE!\n\nThis is PsychoPy',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    adv_intro = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Encoding" ---
    encoding_image = visual.ImageStim(
        win=win,
        name='encoding_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    encoding_audio = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='encoding_audio')
    encoding_audio.setVolume(1.0)
    encoding_text = visual.TextStim(win=win, name='encoding_text',
        text='',
        font='Arial',
        pos=(0, .3), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "FactTest" ---
    facttest_image = visual.ImageStim(
        win=win,
        name='facttest_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, .2), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    facttest_question = visual.TextStim(win=win, name='facttest_question',
        text='',
        font='Open Sans',
        pos=(0, -.1), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    facttest_options = visual.TextStim(win=win, name='facttest_options',
        text='',
        font='Open Sans',
        pos=(0, -.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    facttest_response = keyboard.Keyboard()
    
    # --- Initialize components for Routine "SourceTest" ---
    source_text = visual.TextStim(win=win, name='source_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    source_response = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Exit" ---
    text = visual.TextStim(win=win, name='text',
        text='Thanks for participating!\n\nClick the space bar to quit.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    exit_response = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "IntroText" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('IntroText.started', globalClock.getTime())
    adv_intro.keys = []
    adv_intro.rt = []
    _adv_intro_allKeys = []
    # keep track of which components have finished
    IntroTextComponents = [intro_text, adv_intro]
    for thisComponent in IntroTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IntroText" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *intro_text* updates
        
        # if intro_text is starting this frame...
        if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intro_text.frameNStart = frameN  # exact frame index
            intro_text.tStart = t  # local t and not account for scr refresh
            intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            intro_text.status = STARTED
            intro_text.setAutoDraw(True)
        
        # if intro_text is active this frame...
        if intro_text.status == STARTED:
            # update params
            pass
        
        # *adv_intro* updates
        waitOnFlip = False
        
        # if adv_intro is starting this frame...
        if adv_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            adv_intro.frameNStart = frameN  # exact frame index
            adv_intro.tStart = t  # local t and not account for scr refresh
            adv_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(adv_intro, 'tStartRefresh')  # time at next scr refresh
            # update status
            adv_intro.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(adv_intro.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(adv_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if adv_intro is stopping this frame...
        if adv_intro.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > adv_intro.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                adv_intro.tStop = t  # not accounting for scr refresh
                adv_intro.frameNStop = frameN  # exact frame index
                # update status
                adv_intro.status = FINISHED
                adv_intro.status = FINISHED
        if adv_intro.status == STARTED and not waitOnFlip:
            theseKeys = adv_intro.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _adv_intro_allKeys.extend(theseKeys)
            if len(_adv_intro_allKeys):
                adv_intro.keys = _adv_intro_allKeys[-1].name  # just the last key pressed
                adv_intro.rt = _adv_intro_allKeys[-1].rt
                adv_intro.duration = _adv_intro_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntroTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IntroText" ---
    for thisComponent in IntroTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('IntroText.stopped', globalClock.getTime())
    # the Routine "IntroText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stim/stim.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Encoding" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Encoding.started', globalClock.getTime())
        encoding_image.setImage('stim/'+animal_image)
        encoding_audio.setSound('stim/'+question_audio, secs=6, hamming=True)
        encoding_audio.setVolume(1.0, log=False)
        encoding_audio.seek(0)
        encoding_text.setText(animal_name)
        # keep track of which components have finished
        EncodingComponents = [encoding_image, encoding_audio, encoding_text]
        for thisComponent in EncodingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encoding" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *encoding_image* updates
            
            # if encoding_image is starting this frame...
            if encoding_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encoding_image.frameNStart = frameN  # exact frame index
                encoding_image.tStart = t  # local t and not account for scr refresh
                encoding_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encoding_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                encoding_image.status = STARTED
                encoding_image.setAutoDraw(True)
            
            # if encoding_image is active this frame...
            if encoding_image.status == STARTED:
                # update params
                pass
            
            # if encoding_image is stopping this frame...
            if encoding_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encoding_image.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    encoding_image.tStop = t  # not accounting for scr refresh
                    encoding_image.frameNStop = frameN  # exact frame index
                    # update status
                    encoding_image.status = FINISHED
                    encoding_image.setAutoDraw(False)
            
            # if encoding_audio is starting this frame...
            if encoding_audio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encoding_audio.frameNStart = frameN  # exact frame index
                encoding_audio.tStart = t  # local t and not account for scr refresh
                encoding_audio.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                encoding_audio.status = STARTED
                encoding_audio.play(when=win)  # sync with win flip
            
            # if encoding_audio is stopping this frame...
            if encoding_audio.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encoding_audio.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    encoding_audio.tStop = t  # not accounting for scr refresh
                    encoding_audio.frameNStop = frameN  # exact frame index
                    # update status
                    encoding_audio.status = FINISHED
                    encoding_audio.stop()
            # update encoding_audio status according to whether it's playing
            if encoding_audio.isPlaying:
                encoding_audio.status = STARTED
            elif encoding_audio.isFinished:
                encoding_audio.status = FINISHED
            
            # *encoding_text* updates
            
            # if encoding_text is starting this frame...
            if encoding_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encoding_text.frameNStart = frameN  # exact frame index
                encoding_text.tStart = t  # local t and not account for scr refresh
                encoding_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encoding_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                encoding_text.status = STARTED
                encoding_text.setAutoDraw(True)
            
            # if encoding_text is active this frame...
            if encoding_text.status == STARTED:
                # update params
                pass
            
            # if encoding_text is stopping this frame...
            if encoding_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encoding_text.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    encoding_text.tStop = t  # not accounting for scr refresh
                    encoding_text.frameNStop = frameN  # exact frame index
                    # update status
                    encoding_text.status = FINISHED
                    encoding_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in EncodingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encoding" ---
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Encoding.stopped', globalClock.getTime())
        encoding_audio.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('stim/stim.csv'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "FactTest" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('FactTest.started', globalClock.getTime())
        facttest_image.setImage('stim/'+animal_image)
        facttest_question.setText(question)
        facttest_options.setText(letter_a + choice_a + '\n' + letter_b + choice_b)
        facttest_response.keys = []
        facttest_response.rt = []
        _facttest_response_allKeys = []
        # keep track of which components have finished
        FactTestComponents = [facttest_image, facttest_question, facttest_options, facttest_response]
        for thisComponent in FactTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "FactTest" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *facttest_image* updates
            
            # if facttest_image is starting this frame...
            if facttest_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                facttest_image.frameNStart = frameN  # exact frame index
                facttest_image.tStart = t  # local t and not account for scr refresh
                facttest_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(facttest_image, 'tStartRefresh')  # time at next scr refresh
                # update status
                facttest_image.status = STARTED
                facttest_image.setAutoDraw(True)
            
            # if facttest_image is active this frame...
            if facttest_image.status == STARTED:
                # update params
                pass
            
            # *facttest_question* updates
            
            # if facttest_question is starting this frame...
            if facttest_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                facttest_question.frameNStart = frameN  # exact frame index
                facttest_question.tStart = t  # local t and not account for scr refresh
                facttest_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(facttest_question, 'tStartRefresh')  # time at next scr refresh
                # update status
                facttest_question.status = STARTED
                facttest_question.setAutoDraw(True)
            
            # if facttest_question is active this frame...
            if facttest_question.status == STARTED:
                # update params
                pass
            
            # *facttest_options* updates
            
            # if facttest_options is starting this frame...
            if facttest_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                facttest_options.frameNStart = frameN  # exact frame index
                facttest_options.tStart = t  # local t and not account for scr refresh
                facttest_options.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(facttest_options, 'tStartRefresh')  # time at next scr refresh
                # update status
                facttest_options.status = STARTED
                facttest_options.setAutoDraw(True)
            
            # if facttest_options is active this frame...
            if facttest_options.status == STARTED:
                # update params
                pass
            
            # *facttest_response* updates
            waitOnFlip = False
            
            # if facttest_response is starting this frame...
            if facttest_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                facttest_response.frameNStart = frameN  # exact frame index
                facttest_response.tStart = t  # local t and not account for scr refresh
                facttest_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(facttest_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'facttest_response.started')
                # update status
                facttest_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(facttest_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(facttest_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if facttest_response.status == STARTED and not waitOnFlip:
                theseKeys = facttest_response.getKeys(keyList=['a','b'], ignoreKeys=["escape"], waitRelease=False)
                _facttest_response_allKeys.extend(theseKeys)
                if len(_facttest_response_allKeys):
                    facttest_response.keys = _facttest_response_allKeys[-1].name  # just the last key pressed
                    facttest_response.rt = _facttest_response_allKeys[-1].rt
                    facttest_response.duration = _facttest_response_allKeys[-1].duration
                    # was this correct?
                    if (facttest_response.keys == str(correct_answer)) or (facttest_response.keys == correct_answer):
                        facttest_response.corr = 1
                    else:
                        facttest_response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FactTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "FactTest" ---
        for thisComponent in FactTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('FactTest.stopped', globalClock.getTime())
        # check responses
        if facttest_response.keys in ['', [], None]:  # No response was made
            facttest_response.keys = None
            # was no response the correct answer?!
            if str(correct_answer).lower() == 'none':
               facttest_response.corr = 1;  # correct non-response
            else:
               facttest_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('facttest_response.keys',facttest_response.keys)
        trials_2.addData('facttest_response.corr', facttest_response.corr)
        if facttest_response.keys != None:  # we had a response
            trials_2.addData('facttest_response.rt', facttest_response.rt)
            trials_2.addData('facttest_response.duration', facttest_response.duration)
        # the Routine "FactTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "SourceTest" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('SourceTest.started', globalClock.getTime())
        source_text.setText('Did a male or female voice tell you this fact?\n\na. Male\nb. Female')
        source_response.keys = []
        source_response.rt = []
        _source_response_allKeys = []
        # keep track of which components have finished
        SourceTestComponents = [source_text, source_response]
        for thisComponent in SourceTestComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SourceTest" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *source_text* updates
            
            # if source_text is starting this frame...
            if source_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                source_text.frameNStart = frameN  # exact frame index
                source_text.tStart = t  # local t and not account for scr refresh
                source_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(source_text, 'tStartRefresh')  # time at next scr refresh
                # update status
                source_text.status = STARTED
                source_text.setAutoDraw(True)
            
            # if source_text is active this frame...
            if source_text.status == STARTED:
                # update params
                pass
            
            # *source_response* updates
            waitOnFlip = False
            
            # if source_response is starting this frame...
            if source_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                source_response.frameNStart = frameN  # exact frame index
                source_response.tStart = t  # local t and not account for scr refresh
                source_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(source_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'source_response.started')
                # update status
                source_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(source_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(source_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if source_response.status == STARTED and not waitOnFlip:
                theseKeys = source_response.getKeys(keyList=['a','b'], ignoreKeys=["escape"], waitRelease=False)
                _source_response_allKeys.extend(theseKeys)
                if len(_source_response_allKeys):
                    source_response.keys = _source_response_allKeys[-1].name  # just the last key pressed
                    source_response.rt = _source_response_allKeys[-1].rt
                    source_response.duration = _source_response_allKeys[-1].duration
                    # was this correct?
                    if (source_response.keys == str(correct_answer)) or (source_response.keys == correct_answer):
                        source_response.corr = 1
                    else:
                        source_response.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SourceTestComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SourceTest" ---
        for thisComponent in SourceTestComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('SourceTest.stopped', globalClock.getTime())
        # check responses
        if source_response.keys in ['', [], None]:  # No response was made
            source_response.keys = None
            # was no response the correct answer?!
            if str(correct_answer).lower() == 'none':
               source_response.corr = 1;  # correct non-response
            else:
               source_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('source_response.keys',source_response.keys)
        trials_2.addData('source_response.corr', source_response.corr)
        if source_response.keys != None:  # we had a response
            trials_2.addData('source_response.rt', source_response.rt)
            trials_2.addData('source_response.duration', source_response.duration)
        # the Routine "SourceTest" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_2'
    
    
    # --- Prepare to start Routine "Exit" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Exit.started', globalClock.getTime())
    exit_response.keys = []
    exit_response.rt = []
    _exit_response_allKeys = []
    # keep track of which components have finished
    ExitComponents = [text, exit_response]
    for thisComponent in ExitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Exit" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *exit_response* updates
        waitOnFlip = False
        
        # if exit_response is starting this frame...
        if exit_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exit_response.frameNStart = frameN  # exact frame index
            exit_response.tStart = t  # local t and not account for scr refresh
            exit_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exit_response, 'tStartRefresh')  # time at next scr refresh
            # update status
            exit_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(exit_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(exit_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if exit_response.status == STARTED and not waitOnFlip:
            theseKeys = exit_response.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _exit_response_allKeys.extend(theseKeys)
            if len(_exit_response_allKeys):
                exit_response.keys = _exit_response_allKeys[-1].name  # just the last key pressed
                exit_response.rt = _exit_response_allKeys[-1].rt
                exit_response.duration = _exit_response_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Exit" ---
    for thisComponent in ExitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Exit.stopped', globalClock.getTime())
    # the Routine "Exit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
