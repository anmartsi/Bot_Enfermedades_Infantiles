from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionProvideDiagnosis(Action):

    def name(self) -> str:
        return "action_provide_diagnosis"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        symptoms = tracker.get_slot("symptom")
        body = tracker.get_slot("body")
        severity = tracker.get_slot("severity")

        # Implementa la lógica de diagnóstico basada en los síntomas
        diagnosis = self.diagnose(symptoms, body, severity)
        
        # Imprime el valor de diagnosis para verificar su contenido
        print("Diagnóstico calculado:", diagnosis) 

        # Establece el slot diagnosis con el valor calculado
        return [SlotSet("diagnosis", diagnosis)]

    def diagnose(self, symptoms, body, severity):
        # Ejemplo simple de lógica de diagnóstico
        if "fiebre" in symptoms or "sarpullido" in symptoms or "dolor de garganta" in symptoms or "erupción" in symptoms or "granitos" in symptoms or "llagas en la boca" in symptoms or "heridas" in symptoms or "ampollas" in symptoms or "boca" in body or "pies" in body or "dolor al tragar" in symptoms or "manos" in body or "lengua" in body:
            return "Si tu hijo presenta llagas en la boca o un sarpullido alrededor de la boca, en las manos o pies, podría tratarse de la enfermedad mano-pie-boca.\nSi los síntomas no empeoran, no es necesaria una visita al médico.\nLo más importante es mantener al niño hidratado hasta su recuperación."
        elif "fiebre" in symptoms or "sarpullido" in symptoms or "dolor de garganta" in symptoms or "erupción" in symptoms or "granitos" in symptoms or "lengua inflamada" in symptoms or "lengua roja" in symptoms or "lengua blanca" in symptoms or "pecho" in body or "escalofríos" in symptoms or "cuerpo" in body or "calentura" in symptoms or "alta" in severity or "ronchas" in symptoms:
            return "Si tu hijo tiene la lengua roja, blanca o inflamada, es posible que se haya contagiado de la fiebre escarlatina.\nSe recomienda acudir al médico para obtener un tratamiento antibiótico acorde."
        elif "fiebre" in symptoms or "sarpullido" in symptoms or "moqueo" in symptoms or "piel enrojecida" in symptoms or "cara" in body or "roja" in symptoms or "mejillas" in body or "malestar" in symptoms or "general" in body or "manchas rojas" in symptoms or "articular" in body or "sarpullido" in symptoms or "cuerpo" in body or "como un tomate" in symptoms or "febrícula" in symptoms or "cachetes" in body or "rojos" in symptoms or "enrojecida" in symptoms or "dolor" in symptoms or "articulaciones" in body:
            return "Si tu hijo tiene un sarpullido amplio en diferentes zonas del cuerpo, pero especialmente en las mejillas, lo más probable es que se trate de un eritema infeccioso o enfermedad de la bofetada.\nNo es necesaria una visita al médico.\nMUY IMPORTANTE: Evitar el contacto con gestantes, ya que podría ser perjudicial para el feto."
        elif "fiebre" in symptoms or "diarrea" in symptoms or "vómito" in symptoms or "dolor" in symptoms or "abdominal" in body or "náuseas" in symptoms or "malestar" in symptoms or "estómago" in body or "vomitando" in symptoms or "panza" in body:
            return "Parece una gastroenteritis común.\nAcudir al médico si resulta imposible mantener al niño hidratado."
        elif "tos" in symptoms or "vómitos" in symptoms or "ataques de tos" in symptoms or "convulsiva" in severity or "moqueo" in symptoms or "severa" in severity or "fiebre" in symptoms or "baja" in severity or "dificultad para respirar" in symptoms or "seca" in severity or "fuerte" in severity or "leve" in severity or "intensa" in severity or "mocos" in symptoms or "tosiendo" in symptoms or "mucho" in severity or "vomita" in symptoms:
            return "Si tu hijo no está vacunado contra la tosferina, parece ser el caso.\nAcudir al médico si hay vómitos y el niño tiene dificultad para respirar debido a los ataques de tos."
        elif "fiebre" in symptoms or "sarpullido" in symptoms or "puntos" in symptoms or "costras" in symptoms or "erupción" in symptoms or "ampollas" in symptoms or "picazón" in symptoms or "piel" in body or "malestar" in symptoms or "general" in body or "ronchitas" in symptoms or "ronchas" in symptoms or "granitos" in symptoms or "alta" in severity or "erupciones" in symptoms:
            return "Si tu hijo tiene una erupción de pequeñas costras que causan gran comezón por todo el cuerpo, lo más seguro es que se trate de varicela.\nNo es necesario acudir al médico si los síntomas no empeoran.\nExisten a disposición tratamientos para aliviar el picor."
        elif "fiebre" in symptoms or "alta" in severity or "tos" in symptoms or "sarpullido" in symptoms or "erupción" in symptoms or "manchas" in symptoms or "piel enrojecida" in symptoms or "piel" in body or "conjuntivitis" in symptoms or "moqueando" in symptoms or "ojos rojos" in symptoms or "ojos" in body or "manchitas" in symptoms or "erupciones" in symptoms:
            return "Si la erupción se trata más bien de manchas y no costras (como en el caso de la varicela) y tu hijo no ha recibido la vacuna triple vírica, lo más probable es que se trate de un caso de sarampión.\nNo existe tratamiento y no es necesario acudir al médico si los síntomas no empeoran."
        elif "fiebre" in symptoms or "hinchazón" in symptoms or "malestar" in symptoms or "inflamación" in symptoms or "cara hinchada" in symptoms or "cuello inflamado" in symptoms or "mejilla hinchada" in symptoms or "cara hinchada" in symptoms or "mandíbula" in symptoms or "cuello" in symptoms or "glándulas inflamadas" in symptoms or "malestar" in symptoms or "general" in body or "dolor" in symptoms or "cabeza" in body or "garganta" in body or "hinchado" in symptoms:
            return "Si tu hijo no ha sido vacunado contra las paperas, es muy posible que este sea el caso.\nEs necesario acudir al médico para obtener el tratamiento correspondiente."
        else:
            return "Lamentablemente, los síntomas no coinciden con ninguna enfermedad que conozca, por favor consulta a un médico."

