# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:14:38 2017

@author: ldh
"""

# plan_task.py


def add_plan_task():
    '''
    向系统中添加python脚本计划任务。
    '''
    import win32com.client, sys
    #A constant that specifies a time-based trigger.
    TriggerTypeTime = 1
    #A constant that specifies an executable action.
    ActionTypeExec = 0   
    #********************************************************
    # Create the TaskService object.
    service = win32com.client.Dispatch("Schedule.Service")
    service.Connect()
    #********************************************************
    # Get a folder to create a task definition in. 
    #Dim rootFolder
    rootFolder = service.GetFolder("\\")
    taskDefinition = service.NewTask(0)  
    #Define information about the task.
    #Set the registration info for the task by 
    #creating the RegistrationInfo object.
    regInfo = taskDefinition.RegistrationInfo
    regInfo.Description = "Start notepad at a certain time"
    regInfo.Author = "Author Name"
    
    #********************************************************
    # Set the principal for the task
    principal = taskDefinition.Principal
    
    # Set the logon type to interactive logon
    principal.LogonType = 3
    
    
    # Set the task setting info for the Task Scheduler by
    # creating a TaskSettings object.
    #http://msdn.microsoft.com/en-us/library/windows/desktop/aa383480(v=VS.85).aspx
    settings = taskDefinition.Settings
    settings.Enabled = True #If True, the task is enabled. 
    settings.StartWhenAvailable = True
    settings.Hidden = False #If False, the task will be visible in the UI. The default is False.
    settings.MultipleInstances = 0 # Starts a new instance while an existing instance of the task is running.
    # settings.RunOnlyIfNetworkAvailable = True
    #********************************************************
    # Create a time-based trigger.
    triggers = taskDefinition.Triggers
    trigger = triggers.Create(TriggerTypeTime)
    
    # Trigger variables that define when the trigger is active.
    from datetime import datetime
    from datetime import timedelta
    
    time = datetime.now() + timedelta(0,30)
    startTime = time.strftime('%Y-%m-%dT%H:%M:%S')  #YYYY-MM-DDTHH:MM:SS.
    #time = DateAdd("s", 30, Now)  #start time = 30 seconds from now
    #startTime = XmlTime(time)
    
    time = datetime.now() + timedelta(0,5 *30)
    endTime = time.strftime('%Y-%m-%dT%H:%M:%S') 
    #time = DateAdd("n", 5, Now) #end time = 5 minutes from now
    #endTime = XmlTime(time)
    
    print "startTime :" , startTime
    print "endTime :" , endTime
    
    trigger.StartBoundary = startTime
    trigger.EndBoundary = endTime
    trigger.ExecutionTimeLimit = "PT5M"    #Five minutes
    trigger.Id = "TimeTriggerId"
    trigger.Enabled = True

    #***********************************************************
    # Create the action for the task to execute.
    
    # Add an action to the task to run notepad.exe.
    Action = taskDefinition.Actions.Create( ActionTypeExec )
    Action.Path = "C:\\Windows\\System32\\notepad.exe"
    
    print "Task definition created. About to submit the task..."
    
    #***********************************************************
    # Register (create) the task.
    '''
     参考 http://msdn.microsoft.com/en-us/library/windows/desktop/aa382577(v=VS.85).aspx
    TaskFolder.RegisterTaskDefinition( _
    ByVal path, # The name of the task.
    ByVal definition, # The definition of the task that is registered.
    ByVal flags, _ #0x6 TASK_CREATE_OR_UPDATE
    ByVal userId, _
    ByVal password, _
    ByVal longonType, #3 User must already be logged on. The task will be run only in an existing interactive session.
    [ ByVal sddl ], _
    ByRef task _
  )
    '''
    #
    rootFolder.RegisterTaskDefinition( "Test TimeTrigger", taskDefinition, 6, None,None , 3)
    print "Task submitted."

