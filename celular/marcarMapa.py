import folium, pandas as pd


def abrirArq():
    location = pd.read_csv("locations.csv")
    return location


def criarMapa():
    cidade = folium.Map(location=[-3.062339, -59.973522], zoom_start=12)
    return cidade


def marcarLoc():
    manaus = criarMapa()
    locations = abrirArq()
    for _, local in locations.iterrows():
        folium.Marker(location=[local["lat"], local["long"]]).add_to(manaus)
    manaus.save("manaus.html")

def marcar(mapa, coordenada):
    folium.Marker(location=[float(i) for i in coordenada.split(",")]).add_to(mapa)
    mapa.save("mapa.html")
    
