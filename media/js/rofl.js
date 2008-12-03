dojo.require("dojo.dnd.Source");
dojo.require("dijit.Tooltip");

function highlightTargets()
{
    var props = {
        margin: { start: '0', end: '-1', unit: 'px' },
        borderWidth: { start: '0', end: '1', unit: 'px' }
    };
    dojo.anim("first_column", props, 200);
    dojo.anim("second_column", props, 200);
    dojo.anim("third_column", props, 200);

}

function unhighlightTargets()
{
    var props = {
        margin: { start: '-1', end: '0', unit: 'px' },
        borderWidth: { start: '1', end: '0', unit: 'px' }
    };
    dojo.anim("first_column", props, 200);
    dojo.anim("second_column", props, 200);
    dojo.anim("third_column", props, 200);
}

function init()
{
    var first_column = new dojo.dnd.Source("first_column", {withHandles: true});
    var second_column = new dojo.dnd.Source("second_column");
    var third_column = new dojo.dnd.Source("third_column");
    
    dojo.subscribe("/dnd/start", null, highlightTargets);
    dojo.subscribe("/dnd/cancel", null, unhighlightTargets);
    dojo.subscribe("/dnd/drop", null, unhighlightTargets);
    
    dojo.forEach(dojo.query('.feed_item'), function(node)
    {
        dojo.connect(node, 'onmouseover', function(){
            dojo.removeClass(node.getElementsByTagName('div')[0], 'hidden')
        })
        dojo.connect(node, 'onmouseout', function(){
            dojo.addClass(node.getElementsByTagName('div')[0], 'hidden')
        })
    })

}
dojo.addOnLoad(init);
