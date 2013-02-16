/**
 * Bookmark, Categoryの登録バリデーションチェック
 */
function fnValidCheck(mode){
    var check_flg = true;
    switch(mode) {
        case 'bookmark':
            // 必須チェック
            require_form = {};
            require_form['category'] = $('#bookmark-category').val();
            require_form['url'] = $('#bookmark-url').val();
            require_form['name'] = $('#bookmark-name').val();
            require_flg = requireCheck(mode, require_form);
            // URLチェック
            if(require_flg){
                url_form = {};
                url_form['url'] = $('#bookmark-url').val();
                url_flg = urlCheck(mode, url_form);
            } else {
                url_flg = true;
            }
            // エラーがあったか判定
            if(check_flg != require_flg  || check_flg != url_flg){
                check_flg = false;
            }
            break;
        case 'category':
            // 必須チェック
            require_form = {};
            require_form['name'] = $('#category-name').val();
            check_flg = requireCheck(mode, require_form);
            break;
        case 'page':
            // 必須チェック
            require_form = {};
            require_form['name'] = $('#page-name').val();
            check_flg = requireCheck(mode, require_form);
            break;
        case 'page-edit':
            // 必須チェック
            require_form = {};
            require_form['name'] = $('#page-edit-name').val();
            check_flg = requireCheck(mode, require_form);
            break;
    }
    if(!check_flg){
        return false;
    }
    return true;
}

/**
 * 必須チェック
 */
function requireCheck(mode, list_form){
    var check_flg = true;
    for(var form in list_form){
        if(check_flg){
            if(list_form[form] == ""){
                check_flg = false;
            }
        }
        if(list_form[form] == ""){
            $('#'+mode+'-'+form+'-require-error').show();
            $('#'+mode+'-'+form+'-group').addClass('error');
        } else {
            print 
            $('#'+mode+'-'+form+'-require-error').hide();
            $('#'+mode+'-'+form+'-group').removeClass('error');
        }
    }
    return check_flg;
}

/**
 * URLチェック
 */
function urlCheck(mode, list_form){
    var check_flg = true;
    for(var form in list_form){
        if(check_flg){
            if(list_form[form] == ""){
                check_flg = false;
            }
        }
        re = new RegExp("^[-_.!~*¥'()a-zA-Z0-9;¥/?:¥@&=+¥$,%#]+$");
        if(!list_form[form].match(re)){
            $('#'+mode+'-'+form+'-url-error').show();
            $('#'+mode+'-'+form+'-group').addClass('error');
        } else {
            $('#'+mode+'-'+form+'-url-error').hide();
            $('#'+mode+'-'+form+'-group').removeClass('error');
        }
    }
    return check_flg;
}

