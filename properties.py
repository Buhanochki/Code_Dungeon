base_url = 'textures/first_layer/'
textures = {

}


for i in range(1, 29, 1):
    textures[f"floor_{i}"] = {
        "name": f"f{i}.png",
        "isPass": True,
        "isAnimation": False,
        "isDamage": False,
    }