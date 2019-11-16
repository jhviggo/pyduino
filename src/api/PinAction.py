class PinAction:
    def on_post(self, req, resp, con, action, pin, value):
        if con.lower() == 'digital':
            if action.lower() == 'read':

