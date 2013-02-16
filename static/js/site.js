
function fnAllCheck(){
    if($("#AllCheck").attr('checked')){
        $("input[name='check[]']").attr('checked', 'checked');
    } else {
        $("input[name='check[]']").removeAttr('checked');
    }
}

// 確認後、削除を行う。
function fnDeleteSubmit(form, url){
    if(!window.confirm('一度削除したデータは、元に戻せません。\n削除しても宜しいですか？')){
        return;
    }

    document.forms[form].action = url;
    document.forms[form].submit();
}

// チェックボックスで削除を行う。
function fnCheckBoxDelete(checktag){
    check_flg = 0;
    $(checktag).each(function(){
        if($(this).attr('checked')){
            check_flg = 1;
        }
    });

    if(check_flg == 0){
        alert('チェックボックスが選択されていません');
        return false;
    }

    fnModeSubmit('delete', '', '');
}

// チェックボックスで削除を行う。
function fnDeleteCheckSubmit(form, url, checktag){
    check_flg = 0;
    $(checktag).each(function(){
        if($(this).attr('checked')){
            check_flg = 1;
        }
    });

    if(check_flg == 0){
        alert('チェックボックスが選択されていません');
        return false;
    } else {
        if(!window.confirm('一度削除したデータは、元に戻せません。\n削除しても宜しいですか？')){
            return;
        }
    }

    document.forms[form].action = url;
    document.forms[form].submit();
}

// モードとキーを指定してSUBMITを行う。
function fnModeSubmit(mode, keyname, keyid) {
    switch(mode) {
        case 'delete':
            if(!window.confirm('一度削除したデータは、元に戻せません。\n削除しても宜しいですか？')){
                return;
            }
            break;
        default:
            break;
    }
    document.form1['mode'].value = mode;
    if(keyname != "" && keyid != "") {
        document.form1[keyname].value = keyid;
    }
    document.form1.submit();
}

// アクションとキーを指定してSUBMITを行う。
function fnFormActionSubmit(form, url, keyname, keyid) {
    switch(form) {
        case 'regist-bookmark':
            if(!fnValidCheck('bookmark')){
                return;
            }
            break;
        case 'regist-category':
            if(!fnValidCheck('category')){
                return;
            }
            break;
        case 'regist-page':
            if(!fnValidCheck('page')){
                return;
            }
            break;
        case 'page-edit':
            if(!fnValidCheck('page-edit')){
                return;
            }
            break;
        default:
            break;
    }
    document.forms[form].action = url;
    if(keyname != "" && keyid != "") {
        document.forms[form][keyname].value = keyid;
    }
    document.forms[form].submit();
}
