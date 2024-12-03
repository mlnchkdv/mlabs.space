### Задание по Спецкурсу 5.1

Каждый студент должен по итогу семестра оформить и сдать отчет (`*.docx`) на 12 страниц. Структура отчета следующая:

- Титульник
- Содержание
- Теоретический блок
- Решение и описание задания
- Заключение

Ниже приведены индивидуальные задания на всю группу.

| Студент              | Задание                                                      | Комментарий                                                  |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Барыкина Алина       | Реализовать смарт-контракт для добавления и удаления элементов в массиве. | Используйте динамический массив и функции push/pop для работы с элементами. |
| Бондаренко Ирина     | Создать смарт-контракт с функцией модификации строки, введённой пользователем. | Введите переменную для хранения строки и функцию set для её изменения. |
| Булгакова Анастасия  | Реализовать контракт для хранения и вывода данных пользователей. | Используйте структуру User для хранения имени и баланса, а также массив для хранения пользователей. |
| Быкова Дарья         | Создать контракт с защитой от повторной атаки.               | Реализуйте модификатор, запрещающий повторное выполнение функции до завершения текущего вызова. |
| Волченко Иван        | Реализовать контракт, который позволяет владельцу управлять балансами пользователей. | Введите роли "владелец" и "пользователь". Используйте модификатор onlyOwner для ограничений доступа. |
| Гришанова Алина      | Написать смарт-контракт, реализующий простую форму голосования. | Создайте массив для хранения кандидатов и их голосов. Добавьте функцию для голосования. |
| Гурьянова Дарья      | Реализовать смарт-контракт для управления доступом к функции только для определённых ролей. | Используйте модификаторы для управления доступом.            |
| Елисеев Шамиль       | Создать контракт, подсчитывающий количество транзакций от каждого пользователя. | Используйте mapping для хранения количества транзакций по каждому адресу. |
| Емелин Иван          | Реализовать контракт, предоставляющий доступ к данным только после ввода пароля. | Введите переменную для хранения хеша пароля и функцию проверки введённого значения. |
| Ерохина Ксения       | Написать смарт-контракт для реализации функции случайной генерации чисел с использованием Chainlink. | Изучите документацию Chainlink для генерации случайных чисел. |
| Ершова Виктория      | Создать смарт-контракт для хранения событий с использованием логов. | Реализуйте событие, которое логирует информацию о транзакции, включая отправителя, получателя и сумму. |
| Зайнутдинова Зарина  | Реализовать контракт для расчёта и вывода общей суммы элементов массива. | Используйте цикл для суммирования элементов.                 |
| Зубкова Кристина     | Написать контракт, добавляющий новые строки в массив и удаляющий последний элемент массива. | Реализуйте функции add и remove для работы с массивом строк. |
| Иванова Юлия         | Реализовать контракт с функцией записи данных в blockchain, которые доступны только владельцу. | Используйте переменную storage и модификатор onlyOwner.      |
| Керимов Мурат        | Создать контракт для управления ограниченным доступом пользователей с возможностью добавления и удаления админов. | Используйте mapping для ролей администраторов и функции addAdmin/removeAdmin. |
| Куликова Анна        | Написать контракт для управления токенами с фиксацией событий перевода. | Реализуйте функции transfer и событие Transfer.              |
| Лазаревич Кристина   | Реализовать контракт для учёта количества вызовов функции каждым пользователем. | Используйте mapping для хранения количества вызовов по каждому адресу. |
| Лощинин Вячеслав     | Создать смарт-контракт для управления доступом через многоуровневую систему ролей. | Введите уровни доступа и соответствующие модификаторы.       |
| Макаров Никита       | Написать контракт, выводящий минимальное, максимальное и среднее значение массива. | Реализуйте функции для нахождения минимального, максимального значений и средней величины. |
| Мещерякова Елизавета | Реализовать контракт, проверяющий, является ли введённое число простым. | Используйте цикл для проверки делимости.                     |
| Носкина Анастасия    | Написать смарт-контракт с реализацией функции возвращения всех элементов массива в обратном порядке. | Используйте цикл для создания нового массива в обратном порядке. |
| Ночевный Кирилл      | Реализовать контракт, обеспечивающий атомарность нескольких операций. | Используйте модификатор для обеспечения завершения одной операции перед началом следующей. |
| Овчинников Никита    | Создать контракт для вычисления факториала заданного числа.  | Реализуйте рекурсивную или итеративную функцию.              |
| Поляков Владислав    | Написать смарт-контракт с функцией подсчёта суммы всех чётных элементов массива. | Используйте цикл с проверкой условия на чётность.            |
| Сафрина Кристина     | Реализовать контракт для передачи прав на выполнение функций через передачу токенов. | Реализуйте токен и функцию передачи прав.                    |
| Сенькина Ульяна      | Написать контракт, предоставляющий доступ к функции только после выполнения нескольких условий. | Используйте несколько условий в модификаторе доступа.        |
| Фомичёва Яна         | Реализовать смарт-контракт, который позволяет пользователю запрашивать и получать случайное значение из диапазона. | Используйте Chainlink для генерации случайных чисел.         |
| Ханин Никита         | Создать контракт для управления пользовательскими записями с фиксированным лимитом на одного пользователя. | Введите лимит записей на одного пользователя и функцию добавления записи с проверкой. |





| Студент              | Решение                                                      |
| -------------------- | ------------------------------------------------------------ |
| Барыкина Алина       | ```solidity function add(uint item) public { items.push(item); } function remove() public { items.pop(); }``` |
| Бондаренко Ирина     | ```solidity string private data; function set(string memory newData) public { data = newData; }``` |
| Булгакова Анастасия  | ```solidity struct User { string name; uint balance; } User[] public users;``` |
| Быкова Дарья         | ```solidity modifier noReentrancy() { require(!locked, "Reentrancy detected!"); locked = true; _; locked = false; }``` |
| Волченко Иван        | ```solidity modifier onlyOwner() { require(msg.sender == owner, "You are not the owner!"); _; }``` |
| Гришанова Алина      | ```solidity mapping(string => uint) public votes; function vote(string memory candidate) public { votes[candidate]++; }``` |
| Гурьянова Дарья      | ```solidity modifier onlyAdmin() { require(admins[msg.sender], "You are not an admin!"); _; }``` |
| Елисеев Шамиль       | ```solidity mapping(address => uint) public transactions; function incrementTransactionCount() public { transactions[msg.sender]++; }``` |
| Емелин Иван          | ```solidity bytes32 private passwordHash; function verifyPassword(string memory password) public view returns(bool) { return keccak256(abi.encodePacked(password)) == passwordHash; }``` |
| Ерохина Ксения       | Требуется использовать Chainlink VRF. Реализация на основе их официальной документации. |
| Ершова Виктория      | ```solidity event Transaction(address indexed from, address indexed to, uint amount); function logTransaction(address to, uint amount) public { emit Transaction(msg.sender, to, amount); }``` |
| Зайнутдинова Зарина  | ```solidity function sumArray(uint[] memory arr) public pure returns(uint sum) { for (uint i = 0; i < arr.length; i++) { sum += arr[i]; } return sum; }``` |
| Зубкова Кристина     | ```solidity string[] public strings; function add(string memory newStr) public { strings.push(newStr); } function remove() public { strings.pop(); }``` |
| Иванова Юлия         | ```solidity function store(string memory data) public onlyOwner { storedData = data; }``` |
| Керимов Мурат        | ```solidity mapping(address => bool) public admins; function addAdmin(address admin) public onlyOwner { admins[admin] = true; } function removeAdmin(address admin) public onlyOwner { admins[admin] = false; }``` |
| Куликова Анна        | ```solidity event Transfer(address indexed from, address indexed to, uint value); function transfer(address to, uint value) public { emit Transfer(msg.sender, to, value); }``` |
| Лазаревич Кристина   | ```solidity mapping(address => uint) public calls; function incrementCallCount() public { calls[msg.sender]++; }``` |
| Лощинин Вячеслав     | ```solidity modifier onlyRole(uint role) { require(roles[msg.sender] == role, "Access denied!"); _; }``` |
| Макаров Никита       | ```solidity function min(uint[] memory arr) public pure returns(uint minVal) { minVal = arr[0]; for (uint i = 1; i < arr.length; i++) { if (arr[i] < minVal) minVal = arr[i]; } return minVal; }``` |
| Мещерякова Елизавета | ```solidity function isPrime(uint number) public pure returns(bool) { if (number < 2) return false; for (uint i = 2; i * i <= number; i++) { if (number % i == 0) return false; } return true; }``` |
| Носкина Анастасия    | ```solidity function reverseArray(uint[] memory arr) public pure returns(uint[] memory) { uint[] memory reversed = new uint[](arr.length); for (uint i = 0; i < arr.length; i++) { reversed[i] = arr[arr.length - 1 - i]; } return reversed; }``` |
| Ночевный Кирилл      | ```solidity modifier atomic() { require(!inProcess, "Operation in process!"); inProcess = true; _; inProcess = false; }``` |
| Овчинников Никита    | ```solidity function factorial(uint n) public pure returns(uint) { if (n == 0) return 1; return n * factorial(n - 1); }``` |
| Поляков Владислав    | ```solidity function sumEven(uint[] memory arr) public pure returns(uint sum) { for (uint i = 0; i < arr.length; i++) { if (arr[i] % 2 == 0) sum += arr[i]; } return sum; }``` |
| Сафрина Кристина     | ```solidity function delegate(uint tokenId, address to) public { require(tokens[tokenId].owner == msg.sender, "Not the owner!"); tokens[tokenId].owner = to; }``` |
| Сенькина Ульяна      | ```solidity modifier onlyIf(bool condition) { require(condition, "Condition not met!"); _; }``` |
| Фомичёва Яна         | Требуется использовать Chainlink для генерации случайных чисел. |
| Ханин Никита         | ```solidity uint constant limit = 5; mapping(address => string[]) public records; function addRecord(string memory record) public { require(records[msg.sender].length < limit, "Limit exceeded!"); records[msg.sender].push(record); }``` |