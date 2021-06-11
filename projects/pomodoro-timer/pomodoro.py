import rumps

# TODO: Implement all the TODOs.
# When the application is run, `__init__` is called once in the beginning. The functions
# `start_timer`, `continue_timer`, and `stop_timer` are called when their respective buttons are
# clicked in the application menu. Finally, `tick` is called once every second continuously.
# Tip: Use `rumps.notification(<title>, <subtitle>, <message>)` to send a notification.

class PomodoroTimer(rumps.App):
  def __init__(self):
    '''This method is called when the application starts.'''
    super(PomodoroTimer, self).__init__('🍅')
    # TODO: Uncomment the lines below and fill them in.
    # self.is_timer_running =

  @rumps.clicked('Start New Timer')
  def start_timer(self, _):
    '''This method is called when the "Start Timer" button is clicked.'''
    # TODO: Uncomment the lines below and fill them in.
    # self.seconds_remaining =
    # self.is_timer_running =
    # rumps.notification('Pomodoro Timer', '', <your message here>)

  @rumps.clicked('Continue Timer')
  def continue_timer(self, _):
    '''This method is called when the "Continue Timer" button is clicked.'''
    # TODO: Uncomment the lines below and fill them in.
    # self.is_timer_running =
    # rumps.notification('Pomodoro Timer', '', <your message here>)

  @rumps.clicked('Stop Timer')
  def stop_timer(self, _):
    '''This method is called when the "Stop Timer" button is clicked.'''
    # TODO: Uncomment the lines below and fill them in.
    # self.is_timer_running =
    # rumps.notification('Pomodoro Timer', '', <your message here>)

  @rumps.timer(1)
  def tick(self, _):
    '''This method is called once every second.'''
    # TODO: Fill this in. Depending on `self.is_timer_running`, increment `self.seconds_remaining`
    # accordingly. Use `self.title = <new title>` to display the number of seconds remaining.
    # If `self.seconds_remaining` has reached zero, reset `self.is_timer_running` and notify the
    # user that they should take a break :)
    # BONUS: Display the time remaining in the format "Xm Ys", such as "24m 30s". 
    pass

if __name__ == "__main__":
  PomodoroTimer().run()
