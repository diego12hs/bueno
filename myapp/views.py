from django.http import JsonResponse
import pandas as pd

def get_data(request):
    csv_file = 'TotalFeatures-ISCXFlowMeter.csv'
    df = pd.read_csv(csv_file)
    df_min = df.head()
    return JsonResponse(df_min.to_dict(orient='records'), safe=False)

def get_data_by_id(request, data_id):
    csv_file = 'TotalFeatures-ISCXFlowMeter.csv'
    df = pd.read_csv(csv_file)
    data = df[df['id'] == data_id]
    if data.empty:
        return JsonResponse({'error': 'Dato no encontrado'}, status=404)
    return JsonResponse(data.to_dict(orient='records')[0])
