// 获取指定case_id的用例信息
var CaseInit = function (case_id) {

    function getCaseInfo() {
        // 获取某个用例的信息
        $.post("/interface/get_case_info/", {
            "caseId": case_id,
        }, function (resp) {
            if (resp.success === "true") {
                let result = resp.data;
                console.log("结果", result);
                document.getElementById("req_name").value = result.name;
                document.getElementById("req_url").value = result.url;
                document.getElementById("req_header").value = result.reqHeader;
                document.getElementById("req_parameter").value = result.reqParameter;
                document.getElementById("assert_text").value = result.assertText;

                if (result.reqMethod === "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }

                if (result.reqType === "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }

                // 初始化菜单
                ProjectInit('project_name', 'module_name', result.projectName, result.moduleName);

            }else {
                window.alert(resp.message);
            }
        });
    }
    // 调用getCaseInfo函数
    getCaseInfo();

};