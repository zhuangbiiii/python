import unreal

MeshesPath = "/Game/_TEST_/_StaticMeshTemp_"
ThumPath = "/Game/_TEST_/_TexturesTemp_"


def GenereteThumbnail(static_mesh):
    print(static_mesh.get_thumbnail)


# ��ȡ·����������Դ���б�
all_assets = unreal.EditorAssetLibrary.list_assets(MeshesPath)
# �����Ƕ����ص��ڴ��С�
all_assets_loaded = [
    unreal.EditorAssetLibrary.load_asset(a) for a in all_assets]
# �����б��Խ�������̬�����塣
static_mesh_assets = unreal.EditorFilterLibrary.by_class(
    all_assets_loaded, unreal.StaticMesh)
# �б��е�ÿ����̬�����嶼���д˺�����
list(map(GenereteThumbnail, static_mesh_assets))
