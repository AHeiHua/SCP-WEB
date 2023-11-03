scp_list = [
    "scp-173": {
        "name": "scp-173",
        "des": "出生于轻收容区二楼收容室，杀死你所有看见的人类(只有当人类眨眼的一刻，你会高速移动到他面前，扭断他的脊柱)，当遇到数量多的武装人员，你处于劣势，需要离开此地与其他SCP会合",
        "tag":"scp"
    },
    "scp-096": {
        "name": "scp-096",
        "des": "",
        "tag":"scp"
    },
    "dcp-106": {
        "name": "scp-106",
        "des": "",
        "tag": "scp"
    }
]

def find_scp(scp_name: str):
    if scp_name in scp_list.keys():
        return scp_list[scp_name]
    else:
        return None