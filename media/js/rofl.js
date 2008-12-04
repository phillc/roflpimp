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

function currentState()
{
    first_column = []
    dojo.forEach(dojo.query("#first_column .feed"), function(node){
        first_column.push(node.id.substring(5))
    })
    second_column = []
    dojo.forEach(dojo.query("#second_column .feed"), function(node){
        second_column.push(node.id.substring(5))
    })
    third_column = []
    dojo.forEach(dojo.query("#third_column .feed"), function(node){
        third_column.push(node.id.substring(5))
    })
    return {first: first_column, second: second_column, third: third_column}
}

function sendColumns()
{
    state = currentState();
    dojo.xhrPost({
	method : 'POST',
	content : state,
	url: '/update_user/',
	mimetype: "text/plain"
    });

}

function init()
{
    var first_column = new dojo.dnd.Source("first_column", {withHandles: true});
    var second_column = new dojo.dnd.Source("second_column");
    var third_column = new dojo.dnd.Source("third_column");
    
    dojo.subscribe("/dnd/start", null, highlightTargets);
    dojo.subscribe("/dnd/cancel", null, unhighlightTargets);
    dojo.subscribe("/dnd/drop", null, unhighlightTargets);
    dojo.subscribe("/dnd/drop", null, sendColumns)
    
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
