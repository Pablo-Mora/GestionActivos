import pandas as pd
from app.crud import get_all_empleados_completo
import os

def exportar_datos_a_excel(output_file: str = "static/downloads/reporte_general.xlsx"):
    empleados = get_all_empleados_completo()

    df_empleados = pd.DataFrame([e['empleado'] for e in empleados])
    df_hw = pd.DataFrame([h for e in empleados for h in e['hardware']])
    df_lic = pd.DataFrame([l for e in empleados for l in e['licencias']])
    df_acc = pd.DataFrame([a for e in empleados for a in e['accesos']])

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df_empleados.to_excel(writer, sheet_name="Empleados", index=False)
        df_hw.to_excel(writer, sheet_name="Hardware", index=False)
        df_lic.to_excel(writer, sheet_name="Licencias", index=False)
        df_acc.to_excel(writer, sheet_name="AccesosWeb", index=False)

    return output_file