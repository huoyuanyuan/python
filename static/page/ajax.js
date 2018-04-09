$(function(){
	var start = {
		init:function(){
			console.log("can use")
			this.addEvents();
		},
		addEvents:function(){
			var _self = this;
			$(document).on("click",".jGet",function(){
				_self.get();
			})
			$(document).on("click",".jPost",function(){
				_self.post();
			})
			$(document).on("click",".jJson",function(){
				_self.json();
			})
		},
		get:function(){
			var data = {
				name:"hyy",
				age:18
			}
			var url = "test_get"
			$.ajax({
				type:"GET",
				url:url,
				data:data,
				dataType:"json",
				success:function(data){
					console.log(data)
				}
			})
		},
		post:function(){
			var data = {
				name:"dyp",
				age:18,
			}
			var url = "test_post"
			$.ajax({
				type:"post",
				url:url,
				data:data,
				dataType:"json",
				success:function(data){
					console.log(data)
				}
			})
		},
		json:function(){
			var data = {
				name:'keke',
				age:18
			}
			var url = "test_json"
			$.ajax({
				type:"post",
				url:url,
				data:JSON.stringify(data),
				contentType:"application/json;charset=UTF-8",
				dataType:"json",
				success:function(data){
					console.log(data)
				}
			})
		}
	}

	start.init();
})