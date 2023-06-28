import unreal

MeshesPath = "/Game/_TEST_/_StaticMeshTemp_"
ThumPath = "/Game/_TEST_/_TexturesTemp_"


def GenereteThumbnail(static_mesh):
    print(static_mesh.get_thumbnail)


# 获取路径中所有资源的列表。
all_assets = unreal.EditorAssetLibrary.list_assets(MeshesPath)
# 将它们都加载到内存中。
all_assets_loaded = [
    unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]
# 过滤列表以仅包括静态网格体。
static_mesh_assets = unreal.EditorFilterLibrary.by_class(
    all_assets_loaded, unreal.StaticMesh)
# 列表中的每个静态网格体都运行此函数。
list(map(GenereteThumbnail, static_mesh_assets))
