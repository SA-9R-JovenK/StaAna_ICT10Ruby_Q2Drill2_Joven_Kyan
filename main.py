from pyscript import document

# Initial Halloween Maps
members = {
    "Brimstone",
    "Ghost Fort",
    "Helltower",
    "Harvest Event",
    "Eyeaduct",
    "Mann Manor",
    "Lakeside Event",
    "Monster Bash",
    "Slasher",
    "Graveyard",
    "Cursed Cove",
    "Cauldron",
    "Bonesaw",
    "Devil's Arena",
    "Spineyard"
}

def show_members():
    output = ""
    # Alphabetically organize the maps
    for member in sorted(members):
        output += f"<p>{member}</p>"
    document.getElementById("member_list").innerHTML = output
    document.getElementById("total_members").innerHTML = (
        f"Total Maps: {len(members)}"
    )


def add_member(event):
    map_name = document.getElementById("mapname").value.strip()
    if map_name == "":
        return
    members.add(map_name)
    document.getElementById("mapname").value = ""
    show_members()

# Show the list immediately
show_members()