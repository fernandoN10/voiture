import streamlit as st
from streamlit_option_menu import option_menu
import home, heatmap

#st.set_page_config(
#    page_title=""
#)

class Multiapp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='',
                options=['Home', 'Heatmap']
            )

        for a in self.apps:
            if app == a['title']:
                # Establecer configuraciones de página si es necesario antes de llamar a la función
                a['function']()

if __name__ == '__main__':
    multiapp = Multiapp()

    # Agregar las aplicaciones
    multiapp.add_app('Home', home.app)
    multiapp.add_app('Heatmap', heatmap.app)

    # Ejecutar la aplicación seleccionada
    multiapp.run()