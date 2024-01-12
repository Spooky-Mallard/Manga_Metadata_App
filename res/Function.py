import requests
from typing import Any, Dict, List
import json
from PySide6.QtWidgets import QFrame, QListWidgetItem


def Search(search_text: str, INIT) -> json:
    res: requests.Response = requests.post(
        "https://api.mangaupdates.com/v1/series/search", data={"search": search_text}
    )
    print(res.json())
    show_search_results(res.json(), INIT)


def show_search_results(results: Dict, INIT):
    search_results_panel: QFrame = INIT.get_instance("Search_Results_Panel")
    search_results_panel.gridLayout.addWidget(
        INIT.get_instance("Search_Bar"), 0, 3, 1, 1
    )

    for entry in results.get("results"):
        listwidgetitem: QListWidgetItem = QListWidgetItem(INIT.get_instance("Search_Results"))
        listwidgetitem.setText(entry.get("record").get("title"))
    search_results_panel.show()
    INIT.get_instance("Search_Panel").hide()
