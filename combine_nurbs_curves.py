import maya.cmds as cmds

def combine_nurbs_curves():
    # Get selected curves
    sel = cmds.ls(selection=True, type='transform')
    
    if len(sel) != 2:
        cmds.warning("Please select exactly two NURBS curve transforms.")
        return
    
    curve1 = sel[0]
    curve2 = sel[1]

    # Duplicate both to avoid modifying the original shapes
    dup1 = cmds.duplicate(curve1)[0]
    dup2 = cmds.duplicate(curve2)[0]

    # Parent their shapes under the first duplicate
    shapes = cmds.listRelatives(dup2, shapes=True, fullPath=True)
    for shape in shapes:
        cmds.parent(shape, dup1, shape=True, relative=True)

    # Delete the second duplicate's transform node
    cmds.delete(dup2)

    # Optionally delete construction history and rename
    cmds.delete(dup1, constructionHistory=True)
    cmds.rename(dup1, curve1 + "_combined")

    print("Combined curve created successfully.")

combine_nurbs_curves()
