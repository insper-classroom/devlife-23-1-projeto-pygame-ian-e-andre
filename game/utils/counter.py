class Counter:
    '''
    This class is responsible for the counter.
    '''
    def __init__(self, timer_vel, timer_max, loop, callback_exec):
        '''
        Initializes the class and its attributes.
        '''
        self.timer_count = 0
        self.timer_vel = timer_vel
        self.timer_max = timer_max
        self.loop = loop
        self.callback_exec = callback_exec
        
    def update(self, delta_t):
        '''
        Updates the counter, executing the callback function when 
        the timer reaches the maximum value.
        '''
        self.timer_count += self.timer_vel * delta_t
        
        if (self.timer_count >= self.timer_max):
            if (self.loop):
                self.timer_count = 0
            self.callback_exec()
            