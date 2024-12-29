import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        # Get the active design
        design = app.activeProduct
        
        # Ensure the active product is a Fusion design
        if not isinstance(design, adsk.fusion.Design):
            ui.messageBox('Please make sure you have an active Fusion design open.')
            return
        
        # Get the current active selection set (from the Browser)
        selections = ui.activeSelections
        
        # Check if any bodies are selected in the browser
        if selections.count == 0:
            ui.messageBox('No bodies selected.')
            return
        
        # Log the total number of selections
        ui.messageBox(f'Total selections: {selections.count}')
        
        # Create a list to store the selected bodies
        selected_bodies = []
        
        # Save all selected bodies into the list
        for i in range(selections.count):
            selected_item = selections.item(i)
            if isinstance(selected_item.entity, adsk.fusion.BRepBody):
                selected_bodies.append(selected_item.entity)
            else:
                # Log if the selected item is not a BRepBody
                ui.messageBox(f"Item {i} is not a BRepBody. Skipping update.")
        
        # Now update each body in the list
        for body in selected_bodies:
            try:
                # Append 'white' to the body name
                body.name = 'Blue ' + body.name
            except Exception as e:
                # Log the exception for debugging
                ui.messageBox(f"Error with body {body.name}: {str(e)}")

        # Show a success message
        ui.messageBox('Renaming complete! Selected bodies are now appended with "white".')
        
    except Exception as e:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

run(None)
