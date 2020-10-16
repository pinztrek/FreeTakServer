from FreeTAKServer.controllers.SpecificCoTControllers.SendCoTAbstractController import SendCoTAbstractController
from FreeTAKServer.model.FTSModel.Event import Event
from FreeTAKServer.model.SpecificCoT.SendEmergency import SendEmergency
from FreeTAKServer.controllers.XMLCoTController import XMLCoTController

class SendEmergencyController(SendCoTAbstractController):
    def __init__(self, RawCoT):
        if RawCoT.status == 'on':
            tempObject = super().Event.emergecyOn()
            object = SendEmergency()
            object.status = 'on'
            self.fill_object(object, tempObject, RawCoT)


        elif RawCoT.status == 'off':
            tempObject = super().Event.emergecyOff()
            object = SendEmergency()
            object.status = 'off'
            self.fill_object(object, tempObject, RawCoT)