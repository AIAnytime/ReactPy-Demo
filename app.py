from reactpy import component, html, run, hooks
from pathlib import Path
import json

HERE = Path(__file__)
DATA_PATH = HERE.parent / "2019.json"
data = json.loads(DATA_PATH.read_text())

@component
def ShowDataInfo():
    index, set_index = hooks.use_state(0)

    def handle_click(event):
        set_index(index + 1)

    bounded_index = index % len(data)
    bounded_index = str(int(bounded_index)+1)
    data_item = data[bounded_index]
    overall_rank = data_item["Overall rank"]
    country_or_region = data_item["Country or region"]
    score = data_item["Score"]
    gdp_per_capita = data_item["GDP per capita"]
    social_support = data_item["Social support"]
    healthy_life_expectancy = data_item["Healthy life expectancy"]
    freedom_to_make_life_choices = data_item["Freedom to make life choices"]
    generosity = data_item["Generosity"]
    perceptions_of_corruption = data_item["Perceptions of corruption"]

    return html.div(
        html.button({"on_click": handle_click}, "Next"),
        html.h3("Overall rank: ", overall_rank),
        html.h3("Country or region: ", country_or_region),
        html.h3("Score: ", score),
        html.h3("GDP per capita: ", gdp_per_capita),
        html.h3("Social support: ", social_support),
        html.h3("Healthy life expectancy: ", healthy_life_expectancy),
        html.h3("Freedom to make life choices: ", freedom_to_make_life_choices),
        html.h3("Generosity: ", generosity),
        html.h3("Perceptions of corruption: ", perceptions_of_corruption)
    )

run(ShowDataInfo)