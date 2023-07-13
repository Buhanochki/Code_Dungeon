base_url = 'images/main_layer/'
textures = {

}


for i in range(1, 29, 1):
    textures[f"floor_{i + 1}"] = {
        "name": f"f{i + 1}.png",
        "isPass": True,
        "isAnimation": False,
        "isDamage": False,
    }
