     
    /*var get_status = document.getElementById('status');
    var get_rows = document.getElementById('projects');

    eventlistener();
    
    function eventlistener(){

        get_rows.addEventListener('ready', addclass)
        
    }

    function addclass(e){
        e.stopPropagation()
        console.log("test")
        if(get_status.value === "pending"){
            get_rows.className ='table-danger';

        }else if(get_status.value === "progress"){
            get_rows.className='table-info';
        }else{
            get_rows.className='table.success';}
    }*/
    
    $(document).ready(function(e){
        $("#id_end_date").focusout(function(){
            if ($("#id_end_date").val() < $("#id_start_date").val()){ 
                alert("End Date must be greater or equals to the start date")
                $(".add-pro").prop('disabled', true)}
            else{$(".add-pro").prop('disabled', false)}})
        
        $("#show-hide").click(function(){    
            $("#id_resources").toggle(2000);
        });
    
        $(".resources a:even").css("background-color", "lightblue");
        $(".resources a:odd").css("background-color", "#FFDAB9");

        $("#hide_resources").click(function(e){
            e.preventDefault()
            console.log(2)
            $("#div_id_milestone, #div_id_resources").toggle()
        });

        var err_list = $(".errorlist")
        if (err_list){
            err_list.css("color", "red")
            // $(".add-pro").prop('disabled', true)
        }

        var n_task = $("#new_task").text()
        if(n_task =="Add New Task"){
            $("label[for='id_work_done']").hide()
            $("#id_work_done").hide()
            $("label[for=id_status], #id_status, label[for=id_percentage_completed],#id_percentage_completed").hide()
        }else{
            $("#id_work_done").show()
            $("label[for='id_work_done']").show()
        };
        
        
        var task = $("#new_task")
        var task_start = $("input#id_start_date").html()
        var tsk_start = new Date(task_start).toLocaleDateString()
        var start = $("#start").html()
        var pro_st_date = new Date(start).toLocaleDateString()
        var end = new Date($("#end").text()).toLocaleDateString()
        var end_date = new Date($("input#id_end_date").val()).toLocaleDateString()
        var button = $("input[value='Add-Task']")
        if (task.text()==="Add New Task"){
            $("input#id_start_date").focusout(function(){
                alert(tsk_start)
                alert(pro_st_date)
                if(tsk_start < pro_st_date ){
                    
                    alert("Task cannot start before the parent project")
                    button.prop('disabled',true)
                }else{
                    button.prop('disabled',false)
                }
            })
            $("input#id_end_date").focusout(function(){
                if(end_date > end ){
                    alert("Task cannot end after the parent project")
                    button.prop('disabled',true)
                }else{
                    button.prop('disabled',false)
                }
            })
        }
    })
