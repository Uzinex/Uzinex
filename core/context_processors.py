from typing import Dict

def project_meta(request) -> Dict[str, object]:
    return {
        "PROJECT_NAME": "Uzinex Freelance",
        "NAV_LINKS": [
            {"name": "Home", "url": "home"},
            {"name": "Projects", "url": "projects_list"},
        ],
    }
