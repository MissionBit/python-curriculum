import rumps

# TODO: Implement all the TODOs.
# The functions `start_button_clicked`, `stop_button_clicked`, and `continue_button_clicked` are
# called when their respective buttons are clicked in the application menu. Meanwhile, the function
# `every_second` is called once every second continuously.
# Tip: Use `rumps.notification(<title>, <subtitle>, <message>)` to send a notification.

is_timer_running = False
seconds_remaining = 0
title = '🍅'

def start_button_clicked():
  '''This method is called when the "Start New Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  # is_timer_running =
  # seconds_remaining =
  # rumps.notification('Pomodoro Timer', '', <your message here>)

def stop_button_clicked():
  '''This method is called when the "Stop Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  # is_timer_running =
  # rumps.notification('Pomodoro Timer', '', <your message here>)

def continue_button_clicked():
  '''This method is called when the "Continue Timer" button is clicked.'''
  global is_timer_running, seconds_remaining
  # TODO: Uncomment the lines below and fill them in.
  # is_timer_running =
  # rumps.notification('Pomodoro Timer', '', <your message here>)

def every_second():
  '''This method is called once every second.'''
  global is_timer_running, seconds_remaining, title
  # TODO: Fill this in. Depending on `is_timer_running`, increment `seconds_remaining` accordingly.
  # Use `title = <new title>` to display the number of seconds remaining. If `seconds_remaining` has
  # reached zero, reset `is_timer_running` and notify the user that they should take a break :)
  # BONUS: Display the time remaining in the format "Xm Ys", such as "24m 30s". 

################################ DO NOT MODIFY CODE BELOW THIS LINE ################################

class PomodoroTimer(rumps.App):
  def __init__(self): super(PomodoroTimer, self).__init__(title)

  @rumps.clicked('Start New Timer')
  def start_timer(self, _): start_button_clicked()

  @rumps.clicked('Continue Timer')
  def continue_timer(self, _): continue_button_clicked()

  @rumps.clicked('Stop Timer')
  def stop_timer(self, _): stop_button_clicked()

  @rumps.timer(1)
  def tick(self, _):
    global title
    every_second()
    self.title = title

if __name__ == "__main__":
  PomodoroTimer().run()
