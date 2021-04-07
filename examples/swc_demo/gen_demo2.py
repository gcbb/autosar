import json

dev_mode = False
if dev_mode:
    import os, sys
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    sys.path.insert(0, module_path)
    sys.path.append(os.path.dirname(__file__))
import autosar
import amber
import demo


if __name__ == '__main__':
    ws = autosar.workspace("4.2.2")
    ws.apply(demo.components.Demo2_swc)    
    partition = amber.rte.Partition(ws)
    partition.createComponent('/ComponentTypes/Demo2_swc')    
    with open('derived/rtegen.json', 'w') as fp:
        json.dump(partition.toDict(), fp, sort_keys=True, indent=3)
    generator = amber.rte.generator.TypeGenerator(partition)
    generator.genTypeHeader('derived')
    generator = amber.rte.generator.ComponentGenerator(partition)
    generator.generateHeaders('derived')