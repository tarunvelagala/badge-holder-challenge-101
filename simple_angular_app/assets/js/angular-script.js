var app = angular.module("myNoteApp", []);
    app.controller("myNoteCtrl", function($scope) {
        $scope.message = "";
        $scope.i=1;
        $scope.balance=100;
        $scope.left = function () {
            return $scope.message.length;
        };
        function count_char_inc() {
            if ($scope.message.length >= 16 * $scope.i) {
                $scope.i = $scope.i + 1;
            }
        if($scope.message.length<16*$scope.i)
            {
                $scope.i=$scope.i-1;
            }
            return $scope.i;
        }
        $scope.count=function(){
            return count_char_inc();
        };
        $scope.clear = function() {
            $scope.message = "";
        };
        $scope.send = function() {
            alert("Balance remaining"+" "+$scope.note()+"\n"+"sms charge:"+""+$scope.remain());
        };
        $scope.remain =function () {
            return 2* $scope.message.length ;
        };
        $scope.note =function () {

                $scope.balance-=(2*$scope.message.length);
                if($scope.balance<=0){
                    alert("Low Balance");
                }

            return $scope.balance;
        };
    });
