from octopus.blocktopus.blocks.machines import machine_declaration

class machine_wpi_aladdin (machine_declaration):
    def getMachineClass (self):
        from octopus.manufacturer import wpi
        return wpi.Aladdin

    def getMachineParams (self):
        import json
        try:
            return {
                "syringe_diameter": int(json.loads(self.mutation)['syringe_diameter'])
            }
        except (ValueError, KeyError):
            return {}
            
    @staticmethod
    def get_interface_definition ():
        return {
            "machineTitle": "WPI Aladdin syringe pump",
            "machineDefaultName": "pump",
            "machineVars": [
                { "name": "status", "title": "Status", "type": "String", "readonly": True },
                { "name": "rate", "title": "Flow rate", "type": "Number", "unit": { "options": [['mL/min', 1000], ['uL/min', 1]], "default": 1000 } },
                { "name": "direction", "title": "Direction", "type": "String", "options": ['infuse', 'withdraw'] },
                { "name": "dispensed", "title": "Dispensed volume", "type": "Number", "readonly": True },
                { "name": "withdrawn", "title": "Withdrawn volume", "type": "Number", "readonly": True }
            ],
            "machineOptions": [
                { "name": "syringe_diameter", "title": "Syringe Diameter /mm", "type": "Number", "min": 0 }
            ]
        }
