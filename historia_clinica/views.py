from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import HistoriaClinica
from django.views import View
import json

def historia_clinica_por_documento(request):
    if request.method == 'POST':
        try:
            # Asegúrate de que el contenido de la solicitud sea de tipo application/json
            if request.content_type != 'application/json':
                return JsonResponse({'error': 'Tipo de contenido no admitido'}, status=415)

            data = json.loads(request.body.decode('utf-8'))

            documento_paciente = data.get('documento_paciente')

            # Aquí deberías validar que el campo 'documento_paciente' existe y tiene el formato correcto

            historia_clinica = get_object_or_404(HistoriaClinica, documento_paciente=documento_paciente)

            response_data = {
                'id': historia_clinica.id,
                'documento_paciente': historia_clinica.documento_paciente,
                'documento_doctor': historia_clinica.documento_doctor,
                'descripcion': historia_clinica.descripcion,
                'enfermedad': historia_clinica.enfermedad,
                'fecha_creacion': historia_clinica.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
            }

            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Cuerpo de la solicitud no válido'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

class crear_historia_clinica(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        documento_paciente = data.get('documento_paciente')
        documento_doctor = data.get('documento_doctor')
        descripcion = data.get('descripcion')
        enfermedad = data.get('enfermedad')

        historia_clinica = HistoriaClinica.objects.create(
            documento_paciente=documento_paciente,
            documento_doctor=documento_doctor,
            descripcion=descripcion,
            enfermedad=enfermedad
        )

        response_data = {
            'id': historia_clinica.id,
            'documento_paciente': historia_clinica.documento_paciente,
            'documento_doctor': historia_clinica.documento_doctor,
            'descripcion': historia_clinica.descripcion,
            'enfermedad': historia_clinica.enfermedad,
            'fecha_creacion': historia_clinica.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        }

        return JsonResponse(response_data)