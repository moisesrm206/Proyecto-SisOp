import os
import runpy


if __name__ == "__main__":
	raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	ruta_interfaz = os.path.join(raiz_proyecto, "gui", "interfaz.py")
	runpy.run_path(ruta_interfaz, run_name="__main__")
	