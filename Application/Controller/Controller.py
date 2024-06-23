
def NewController(client, config, controllers):
    return Controller(client, config, controllers)

class Controller:
    def __init__(self, client, config, controllers):
        self.client = client
        self.config = config
        self.controllers = controllers
        print('!! Controller initialized')

    def run(self):
        # self.controllers[0].run()
        for controller in self.controllers:
            print(controller)
            controller.run()

