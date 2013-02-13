/**
 * カテゴリのイベント処理
 */
$('.dragbox').each(function(){
    $(this).hover(function(){
        // $(this).find('h2').addClass('subcollapse');
    }, function(){
        // $(this).find('h2').removeClass('subcollapse');
    })
    .find('h2').hover(function(){
        $(this).find('.configure').css('visibility', 'visible');
    }, function(){
        $(this).find('.configure').css('visibility', 'hidden');
    })
    .end().find('.configure').css('visibility', 'hidden');

    $(this).find('.category-title').click(function(){
        cate = $(this).parent().parent().attr('id');
        $('#'+cate+' .dragbox-content').slideToggle();
    });

    $(this).find('.configure').click(function(){
        cate = $(this).parent().parent().attr('id');
        $('#'+cate+' .category-color').slideToggle(0);
    });
});

/**
 * カテゴリ位置の移動
 */
var beginColumn;
var beginRow;
var otherColumnFlg = false;
var sortOrder = [];
$('.column').sortable({
    connectWith: '.column',
    handle: 'h2',
    cursor: 'move',
    placeholder: 'placeholder',
    forcePlaceholderSize: true,
    opacity: 0.4,
    start: function(event, ui){
        beginColumn = event.currentTarget.id;
        beginRow = ui.item.attr('id');

    },
    receive: function(event, ui){
        otherColumnFlg = true;
    },
    update: function(event, ui){
        var sortOrder = [];
        $('.column').each(function(i){
            var itemOrder = $(this).sortable('toArray');
            var columnId = $(this).attr('id');
            sortOrder[i] = itemOrder.toString();
        });
        fnSwapCategory(sortOrder);
    }
})
.disableSelection();

function fnSwapCategory(sortOrder){
    token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        type: "POST",
        url: "/swap_category/",
        data: {"csrfmiddlewaretoken": token,
               "column-1": sortOrder[0],
               "column-2": sortOrder[1],
               "column-3": sortOrder[2],
               "beginColumn": beginColumn,
               "beginRow": beginRow,
               "otherColumnFlg": otherColumnFlg
              },
        dataType: "json",
        async: false,
        success: function(response){}
    });
    return false;
}

/**
 * カテゴリ開閉の状態維持
 */
$('.category-title').click(function(){
    
    category_id = $(this).parent().attr('id');
    token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        type: "POST",
        url: "/tag_open/",
        data: {"csrfmiddlewaretoken": token,
               "category_id": category_id
              },
        dataType: "json",
        async: false,
        success: function(response){}
    });
    return false;
});

/**
 * カテゴリ背景色の変更
 */
$('.colors li').click(function(){
    category_id = $(this).parent().parent().parent().attr('id');
    color = $(this).attr('class');
    token = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
        type: "POST",
        url: "/update_color/",
        data: {"csrfmiddlewaretoken": token,
               "category_id": category_id,
               "color": color
              },
        dataType: "json",
        async: false,
        success: function(response){
                    classData = $('#' + category_id).attr('class');
                    var arrClass = classData.split( /\s/ );
                    for (var i = 0; i < arrClass.length; i++){
                        if(arrClass[i].match(/^color-/)){
                            $('#' + category_id).removeClass(arrClass[i]);
                        }
                    }
                    $('#' + category_id).addClass(color);
                 }
    });
    return false;
});

